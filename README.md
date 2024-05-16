# example-serverless
An example repo to demonstrate cloud function support in Pants

See [pantsbuild.org](https://www.pantsbuild.org/docs) for much more detailed documentation.

# Running Pantsbuild

You run Pants goals using the `pants` launcher binary, which will bootstrap the
version of Pants configured for this repo if necessary.

See [here](https://www.pantsbuild.org/docs/installation) for how to install the `pants` binary.

Use `pants --version` to see the version of Pants configured for the repo (which you can also find
in `pants.toml`).


# Goals

Pants commands are called _goals_. You can get a list of goals with

```
pants help goals
```

## Example Goals
The following goals are configured in this repo.

Run Formatter and linters:
```
pants lint fmt ::
pants --changed-since=HEAD lint fmt :: # Only run on changed files
```

Run formatter and linters with fixes:
```
pants fix ::
pants --changed-since=HEAD fix :: # Only run on changed files
```

Run Tests
```
pants test ::
pants --changed-since=HEAD :: # Only run on changed files
```

Package AWS Lambda Zip files
```
pants package ::
```

Most goals take arguments to run on. To run on a single directory, use the directory name with `:`
at the end. To recursively run on a directory and all its subdirectories, add `::` to the end.
