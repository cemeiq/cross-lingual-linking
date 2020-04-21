from doc_linking import get_test_dataset, get_topic_model_similar_docs_and_distance, get_cr5_similar_docs_and_distance, get_wasserstein_similar_docs_and_distance
from doc_linking import save_distance_results
import json
import os

max_articles = 100
test_year = 2013

print("Opening test data")
aligned_path = "aligned_articles_2013_2015_monthly.json"
aligned_data = json.load(open(aligned_path, 'r'))

for test_month in list(range(0,12)):
    print("* Running document linking for Month", test_month, "- Year", test_year)
    fi_articles, sv_articles, fi_keys, sv_keys, sv_keys_dict, actual_related = get_test_dataset(aligned_data, num_articles=max_articles, month=test_month, year=test_year)

    # # Get Topic Model predictions and distances
    model_name = "yle_100topics_5"
    results_path = "results/" + model_name + "_" + str(test_year) + "_" + str(test_month) + "_iter"
    if os.path.exists(results_path + ".pkl") == False:
        model_filepath = "trained_models/" + model_name
        tm_dist, tm_predictions = get_topic_model_similar_docs_and_distance(model_filepath, fi_articles, sv_articles)
        save_distance_results(tm_dist, tm_predictions, fi_keys, sv_keys, sv_keys_dict, actual_related, out_filepath=results_path)

    # # Get Cr5 predictions and distances
    # results_path = "results/cr5_" + str(test_year) + "_" + str(test_month) + "_2"
    # if os.path.exists(results_path + ".pkl") == False:
    #     cr5_dist, cr5_predictions = get_cr5_similar_docs_and_distance(fi_keys, sv_keys, sv_keys_dict)
    #     save_distance_results(cr5_dist, cr5_predictions, fi_keys, sv_keys, sv_keys_dict, actual_related, out_filepath=results_path)

    # # Get Wasserstein predictions and distances
    # entropic_reg = 0.01
    # results_path = "results/wass_" + str(test_year) + "_" + str(test_month) + "_entropic"
    # if os.path.exists(results_path + ".pkl") == False:
    #     wass_dist, wass_pred = get_wasserstein_similar_docs_and_distance(fi_articles, sv_articles, chunk_size=10, entropic_reg=entropic_reg)
    #     wass_predictions = [list(w) for w in wass_pred]
    #     save_distance_results(wass_dist, wass_predictions, fi_keys, sv_keys, sv_keys_dict, actual_related, out_filepath=results_path)




