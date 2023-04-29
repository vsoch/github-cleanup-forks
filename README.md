# GitHub Cleanup Forks

> Cleanup, cleanup, everybody cleanup! 🧼️

I like to keep my GitHub (personal account) tidy in not saving forks that
I've finished with. I was going through the web interface to do this,
but realized it would be much easier to try on the command line! So I made this
tool, which you can run to loop through your forks (for a username or organization)
and say yes/no to each of them.

Still run this with caution, as deleting is not possible to undo (as far as I know!)

## Usage

First, export a GitHub personal access token to the environment.

```bash
export GITHUB_TOKEN=xxxxxxxxxxxxx
```

**Important** this needs to be a relatively new GitHub token with the `delete_repo` scope.
And then run the script, providing your username or organization.

```bash
$ python cleanup.py vsoch
```

The script will find your repos, ensure we are filtered to forks, and then
prompt you if you want to delete each. You can say yes/no, and then see the status
of the request (204 means deleted):

```bash
...
Delete fork vsoch/bids-validator? (yes/no)? yes
<Response [204]>
Delete fork vsoch/bssw-tutorial.github.io? (yes/no)? no
Delete fork vsoch/builder? (yes/no)? yes
<Response [204]>
```

Happy cleaning!
