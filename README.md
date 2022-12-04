### South Jakarta House Pricing Prediction

by Edycakra Immanuel Sinaga

- A simple machine learning app built with Flask showcasing the implementation of Linear Regression to predict house price in South Jakarta. Dataset is gathered from OLX website.

- ML App: https://jakselhouseprice.herokuapp.com

### Data Preparation and Preprocessing

![alt text](https://github.com/edycakra/jaksel_house_pricing/blob/main/docs/step0.png)

### Feature Engineering

![alt text](https://github.com/edycakra/jaksel_house_pricing/blob/main/docs/step1.png)

### Model

![alt text](https://github.com/edycakra/jaksel_house_pricing/blob/main/docs/step2.png)

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

![alt text](https://github.com/edycakra/jaksel_house_pricing/blob/main/docs/step3.png)
