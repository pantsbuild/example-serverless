python_requirement(
    name="jmespath",
    requirements=["jmespath"],
)

python_requirements(
    name="root",
    source="pyproject.toml",
    overrides={
        "aws-lambda-powertools": {"dependencies": [":jmespath"]},
    },
)

