import difflib
import os
import matplotlib.pyplot as plt

from tqdm import tqdm


alarm_match_percent = 70
repo_path = "esimerkki-projekti-v1"
dir_path = "esimerkki-projekti-v1/harjoitustehtavat/"
repo_url = "https://gitlab.labranet.jamk.fi/TTOS0100/esimerkki-projekti-v1"


if not os.path.exists(repo_path):
    os.system("git clone {}".format(repo_url))
else:
    os.chdir(repo_path)
    os.system("git pull")
    os.chdir("..")


def save_similar_filepaths(path1, path2):
    with open("similar_files.txt", "a") as f:
        f.write("{}\n{}\n\n".format(path1, path2))

    return path1, path2


def compare(dataset1, dataset2, path1, path2, saved_pairs):
    path1 = path1.split("/")[-1]
    path2 = path2.split("/")[-1]
    pair = (path1, path2)
    if pair not in saved_pairs and (pair[1], pair[0]) not in saved_pairs:
        match = difflib.SequenceMatcher(None, dataset1, dataset2)

        match_percent = match.ratio() * 100
        match_percents.append(match_percent)

        if match_percent > alarm_match_percent:
            return save_similar_filepaths(path1, path2)


def get_file_paths():
    return list(map(lambda x: os.path.join(dir_path, x), os.listdir(dir_path)))


def clear_similar_file():
    with open("similar_files.txt", "w") as f:
        f.write("")


def plot_percents():
    plt.plot(match_percents)
    plt.show()


if __name__ == "__main__":
    clear_similar_file()
    filepaths = get_file_paths()
    saved_pairs = []
    match_percents = []

    for path1 in tqdm(filepaths):
        for path2 in filepaths:
            if path1 != path2:
                with open(path1, "rb") as f1:
                    dataset1 = f1.read()

                with open(path2, "rb") as f2:
                    dataset2 = f2.read()

                pair = compare(dataset1, dataset2, path1, path2, saved_pairs)
                if pair:
                    saved_pairs.append(pair)

    plot_percents()
