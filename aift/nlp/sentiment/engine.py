def analyze(text:str, engine:str='ssense', return_json:bool=True):
    if engine == 'emonews':
        from aift.nlp.sentiment.emonews import analyze
        return analyze(text, return_json=return_json)
    elif engine == 'ssense':
        from aift.nlp.sentiment.ssense import analyze
        return analyze(text, return_json=return_json)
    elif engine == 'thaimoji':
        from aift.nlp.sentiment.thaimoji import analyze
        return analyze(text, return_json=return_json)
    elif engine == 'cyberbully':
        from aift.nlp.sentiment.cyberbully import analyze
        return analyze(text, return_json=return_json)
    else:
        raise ValueError(
            f"""Analyzer \"{engine}\" not found."""
        )
