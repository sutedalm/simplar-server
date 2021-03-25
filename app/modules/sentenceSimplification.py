from access.preprocessors import get_preprocessors
from access.resources.prepare import prepare_models
from access.simplifiers import get_fairseq_simplifier, get_preprocessed_simplifier
from access.text import word_tokenize
from access.utils.helpers import yield_lines, write_lines, get_temp_filepath, mute


def evaluate_batch(input: [str]) -> [str]:
    # Usage: python generate.py < my_file.complex
    # Read from stdin
    source_filepath = get_temp_filepath()
    write_lines([word_tokenize(line) for line in input], source_filepath)

    # Load best model
    best_model_dir = prepare_models()
    recommended_preprocessors_kwargs = {
        'LengthRatioPreprocessor': {'target_ratio': 0.95},
        'LevenshteinPreprocessor': {'target_ratio': 0.75},
        'WordRankRatioPreprocessor': {'target_ratio': 0.75},
        'SentencePiecePreprocessor': {'vocab_size': 10000},
    }

    preprocessors = get_preprocessors(recommended_preprocessors_kwargs)
    simplifier = get_fairseq_simplifier(best_model_dir, beam=8)
    simplifier = get_preprocessed_simplifier(simplifier, preprocessors=preprocessors)
    # Simplify
    pred_filepath = get_temp_filepath()

    with mute():
        simplifier(source_filepath, pred_filepath)

    return list(yield_lines(pred_filepath))
