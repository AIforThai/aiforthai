def similarity(text:str, model:str='', numword='5', engine:str='thaiwordsim', return_json:bool=True):
    if engine == 'wordapprox':
        from aift.nlp.similarity.word_approximation import word_approx
        if model == '':
            return word_approx(text, model='royin', return_json=return_json)
        else:
            return word_approx(text, model=model, return_json=return_json)

    elif engine == 'thaiwordsim':
        from aift.nlp.similarity.word_similarity import similarity
        if model == '':
            return similarity(text, model='thwiki', numword=str(numword), return_json=return_json)
        else:
            return similarity(text, model=model, numword=str(numword), return_json=return_json)
    else:
        raise ValueError(
            f"""Model similarity \"{engine}\" not found."""
        )

