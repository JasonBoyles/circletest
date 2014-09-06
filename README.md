# circletest
A simple script which triggers [CircleCI](https://circleci.com/) builds and
returns a status indicating success or failure.

## Installation
    pip install git+https://github.com/JasonBoyles/circletest

## Usage
    circletest [-h] [-p POLL_INTERVAL] [-t CCI_TOKEN] github_organization \
    github_repo_name [git_reference]

All output is sent to stderr, so tack `2>/dev/null` on the end of your command
if you require silence.

### return values
0 indicates success, all values >0 failure.

### positional arguments
  * `github_organization`: the Github username or organization under which the repo lives
  * `github_repo_name`: the name of the repo
  * `git_reference`: git branch/sha/tag on which to run tests (optional, defaults to `master`)

### flags
  * `-p POLL_INTERVAL`, `--poll-interval POLL_INTERVAL`: the number of seconds
  to sleep between each build status poll (optional, defaults to 10)
  * `-t CCI_TOKEN`, `--cci-token CCI_TOKEN`: a valid CircleCI access token
  (optional when the token is supplied in the environment variable `CCI_TOKEN`,
    if you don't already have one, tokens can be generated or downloaded from your [CircleCI account settings page](https://circleci.com/account/api) )

### Examples
Run tests against `https://github.com/mygitusername/mygitrepo`, `master` branch,
supplying the CircleCI token via environment variable:
```
$ export CCI_TOKEN=0123456789abcdef0123456789abcdef
$ circletest mygitusername mygitrepo
```
Run tests against `https://github.com/mygitusername/mygitrepo`, `master` branch,
supplying the CircleCI token via the command line:
```
$ circletest --cci-token=0123456789abcdef0123456789abcdef mygitusername mygitrepo
```
You must supply a valid CircleCI token, either via the command line, or
the environment variable `CCI_TOKEN`. Following examples assume the presence of
this environment variable.

Run tests against the git branch `add-new-feature`:
```
$ circletest mygitusername mygitrepo add-new-feature
```
Run tests against a specific git commit `d5f1459da3f2342f4e0388a4a1aa9d9c5a1b2ee7`:
```
circletest mygitusername mygitrepo d5f1459da3f2342f4e0388a4a1aa9d9c5a1b2ee7
```
