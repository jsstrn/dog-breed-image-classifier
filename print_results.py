#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
from prettytable import PrettyTable


def print_results(pet_labels, stats, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      pet_labels - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      stats - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    total_images = stats.get('n_images')
    total_dog_images = stats.get('n_dogs_img')
    total_non_dog_images = stats.get('n_notdogs_img')

    correct_dogs = stats.get('n_correct_dogs')
    correct_non_dogs = stats.get('n_correct_notdogs')
    correct_breed = stats.get('n_correct_breed')

    correct_non_dogs_percent = stats.get('pct_correct_notdogs')
    correct_dogs_percent = stats.get('pct_correct_dogs')
    correct_breeds_percent = stats.get('pct_correct_breed')
    match_percent = stats.get('pct_match')

    t = PrettyTable(header=False)
    t.add_row(['total images', total_images])
    t.add_row(['total dog images', total_dog_images])
    t.add_row(['total non-dog images', total_non_dog_images])
    print(t)

    t = PrettyTable()
    t.field_names = ['cnn model', '% correct not dogs', '% correct dogs', '% correct breeds', '% match labels']
    t.add_row([
        model,
        get_percent_format(correct_non_dogs_percent),
        get_percent_format(correct_dogs_percent),
        get_percent_format(correct_breeds_percent),
        get_percent_format(match_percent),
    ])
    print(t)

    if print_incorrect_dogs and ((correct_dogs + correct_non_dogs) is not total_images):
        print_incorrectly_classified_dog_images(pet_labels)

    if print_incorrect_breed and (correct_dogs is not correct_breed):
        print_incorrectly_classified_dog_breeds(pet_labels)


def get_percent_format(value):
    return str(round(value, 3)) + '%'


def print_incorrectly_classified_dog_images(pet_labels):
    print("incorrectly classified dog images:".center(100))

    t = PrettyTable()
    t.field_names = ['real', 'classifier']

    for key, values in pet_labels.items():
        label, classification, match, labeled_as_dog, classified_as_dog = values
        if (match == 0) and sum([labeled_as_dog, classified_as_dog]) == 1:
            t.add_row([label, classification])

    print(t)


def print_incorrectly_classified_dog_breeds(pet_labels):
    print("incorrectly classified dog breeds:".center(100))

    t = PrettyTable()
    t.field_names = ['real', 'classifier']

    for key, values in pet_labels.items():
        label, classification, match, labeled_as_dog, classified_as_dog = values
        if (match == 0) and sum([labeled_as_dog, classified_as_dog]) == 2:
            t.add_row([label, classification])

    print(t)
