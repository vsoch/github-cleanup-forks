import os
import sys
import requests


token = os.environ.get("GITHUB_TOKEN")
if not token:
    sys.exit("You are required to export GITHUB_TOKEN")

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token {}".format(token),
}


def confirm_action(question, force=False):
    """confirm if the user wants to perform a certain action

    Parameters
    ==========
    question: the question that will be asked
    force: if the user wants to skip the prompt
    """
    if force is True:
        return True

    response = input(question + " (yes/no)? ")
    while len(response) < 1 or response[0].lower().strip() not in "ynyesno":
        response = input("Please answer yes or no: ")

    if response[0].lower().strip() in "no":
        return False
    return True


def main(user):
    """
    Cleanup one or more repos (that are forked) for a user account.
    """
    url = "https://api.github.com/users/{}/repos".format(user)
    forks = []
    while True:
        print(url)
        listing = requests.get(
            url, headers=headers, params={"per_page": 100, "fork": True}
        )
        # Double check that are forks!
        forks += [x["full_name"] for x in listing.json() if x["fork"] is True]
        if not listing.links.get("next"):
            break
        url = listing.links["next"]["url"]

    print(f"Found {len(forks)} forks!")

    url = "https://api.github.com/repos/"
    for fork in forks:
        path = os.path.join(url, fork)
        if not confirm_action(f"Delete fork{fork}?"):
            continue
        res = requests.delete(path, headers=headers)
        print(res)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(
            "Please provide the username or organization name as the only argument."
        )
    main(sys.argv[1])
