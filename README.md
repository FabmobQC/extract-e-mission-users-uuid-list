# Script to extract users from e-mission-server Database before a date


## Usage:
Create an .env file that contains the url to the server example:

```
{
        "url": "mongodb://DATABASE_USER:PASSWORD@HOST:27017/DATABASE_NAME"
}
```

Then execute the following command where the -d parameter should be a date using the Iso format:

`python main.py -d '2022-04-29T00:00:00.000Z'`
