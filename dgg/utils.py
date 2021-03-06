from bs4 import Doctype, Tag



def delta_sum(steps):
    return sum([s.delta for s in steps])


def clean_soup(soup):
    _remove_doctype(soup)
    _remove_nontags(soup)
    return soup


def _remove_doctype(soup):
    to_extract = [e for e in soup if isinstance(e, Doctype)]
    for e in to_extract:
        e.extract()
    return soup


def _remove_nontags(soup):
    to_extract = [e for e in soup if not isinstance(e, Tag)]
    for e in to_extract:
        e.extract()
    return soup
