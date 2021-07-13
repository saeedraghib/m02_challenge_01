# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, loans):
    """Write the list of loans to a CSV file to the path provided.

    Args:
        csvpath (Path): The csv file path to write to
        loans: List of loans that the user qualifies for

    """
    with open(csvpath, "w", newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        # Loop and read each row in the list
        for row in loans:
            # write each row to the file
            csvwriter.writerow(row)