### South Jakarta House Pricing Prediction

by Edycakra Immanuel Sinaga

- ML App: https://jakselhouseprice.herokuapp.com

### Data Preparation and Preprocessing

### Feature Engineering

### Model

### API Message and Response

- **BASE URL**

  https://jakselhouseprice.herokuapp.com

- **URL**

  `/predict_api`

- **Method:**

  `POST`

- **Data Params Sample**

```
{
    "data": {
        "NBED": 3,
        "NBATH": 3,
        "NFLOOR": 2,
        "BLDAR": 134,
        "LNDAR": 130,
        "CERT": "SHM",
        "LOC": "Pasar Minggu"
    }
}
```

- **Success Response:**

  - **Status:** 200 <br />
    **Content:** <br />
    `1622404393.874084 `
