import pprint
from craigslist import CraigslistForSale

class CLSearcher(object):
    def __init__(self):
        pass

    def search(self, search_term):
        master_results = []
        results = CraigslistForSale(filters={'query': search_term, 'posted_today': True})
        for result in results.get_results(sort_by='newest', geotagged=True):
            pprint.pprint(result)
            master_results.append(result)

        return master_results
