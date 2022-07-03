# 42api-scraping

## Install

Requires python3.1+, and pip.

1. Install (with the Makefile):

```sh
make
```

2. Copy `default.yml` and paste to `local.yml` in `./app/config`, replace `{SECRET}` with our secret data. You have to make a new application in [the 42 API](https://profile.intra.42.fr/oauth/applications/new) to get your `cid` and your `secret`.

## Usage

### Run

```sh
make run
```
