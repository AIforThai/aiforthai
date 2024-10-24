def tokenize(text:str, normalize:bool=False, return_json:bool=True, engine:str='trexplus'):
    if engine == 'lexto':
        from aift.nlp.tokenizer.lexto import tokenize
        return tokenize(text, normalize=normalize, return_json=return_json)
    elif engine == 'trexplus':
        from aift.nlp.tokenizer.trexplus import tokenize
        return tokenize(text, return_json=return_json)
    elif engine == 'trexplusplus':
        from aift.nlp.tokenizer.trexplusplus import tokenize
        return tokenize(text, return_json=return_json)
    else:
        raise ValueError(
            f"""Tokenizer \"{engine}\" not found."""
        )
