import sqlite3
import re
from contextlib import closing


class Repository:
    def query(self, term: str):
        with closing(sqlite3.connect('dict_db')) as conn:
            with closing(conn.cursor()) as cursor:                
                cursor.execute('SELECT * FROM dict_table WHERE dict_table MATCH ? ORDER BY MATCHINFO(dict_table, \'x\') DESC LIMIT 200;', [term])
                rows = cursor.fetchall()
                return rows


class TranslationService:
    repository = Repository()

    def translate(self, term: str, limit: int, page: int) -> dict:
        rows = self.repository.query(term)
        result = []
        for r in rows:
            entry = r[0].split('::')
            german = self.break_examples(entry[0])
            english = self.break_examples(entry[1])
            entry = {}
            entry['german'] = german
            entry['english'] = english
            result.append(entry)     

        result = self.sort(result, term)
        start = page * limit
        end = (page + 1) * limit
        if end > len(result):
            end = len(result)
        if (start > end):
            start = end        
        return {'search_term':term, 'count':len(result), 'limit':limit, 'page':page, 'has_more': len(result) > end , 'results':result[start:end]}        
    
    def break_examples(self, entry:str) -> dict:
        split = entry.split('|')
        if (len(split) > 1):            
            return {'term':split[0].strip(), 'examples': [s.strip() for s in split[1:len(split)]]}
        else:
            return {'term':split[0].strip(), 'examples':None}


    def sort(self, result:list, term:str)-> list:
        last_swap = -1
        for i in range(0, len(result)):
            german = result[i]['german']['term']
            english = result[i]['english']['term']
            swapped = False
            
            g = self.remove_non_term_chars(german)
            g_terms = g.split(';')
            for t in g_terms:
                if t.strip().lower() == term.lower() and (last_swap + 1) < len(result):
                    swapped = True
                    last_swap += 1
                    temp = result[last_swap]                    
                    result[last_swap] = result[i]
                    result[i] = temp
            if (swapped):
                continue

            e = self.remove_non_term_chars(english)
            e_terms = e.split(';')
            for t in e_terms:
                if t.strip().lower() == term.lower() and (last_swap + 1) < len(result):
                    swapped = True
                    last_swap += 1
                    temp = result[last_swap]                    
                    result[last_swap] = result[i]
                    result[i] = temp
        return result


    def remove_non_term_chars(self, input: str) -> str:
        result = re.sub(r'\((.*?)\)', '', input)
        result = re.sub(r'\[(.*?)\]', '', result)
        result = re.sub(r'\{(.*?)\}', '', result)
        result = re.sub(r'\n', '', result)
        return result.strip()
                
        


        