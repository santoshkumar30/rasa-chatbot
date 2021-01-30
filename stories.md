## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot


## customer form
* customer_query
    - customer_form
    - form{"name": "customer_form"}
    - form{"name": null}
    - utter_slots_values


## how doing
* ask_howdoing
    - utter_ask_howdoing

## builder
* ask_builder
    - utter_ask_builder

## language bot
* ask_languagesbot
    - utter_ask_languagesbot

## how old
* ask_howold
    - utter_ask_howold
