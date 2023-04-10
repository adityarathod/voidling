import concurrent.futures

import requests

DATA_SERVICE_TEST_URL = "http://localhost:8000/lore_question/"

LORE_TESTS = [
    "Does Aurelion Sol have any equals?",
    "What species is Ahri?",
    "What did Rengar do to his father?",
    "Is Belveth a dark cancer?",
    "Is Heimerdinger a professor?",
    "What is Tibbers?",
    "What is Kayn's weapon?",
    "Which person wields a trident?",
    "In what way is Jhin a monster?",
    "Who is called 'the blind monk'?",
    "What is Lux's power?",
    "What type of animal is Rammus?",
]


def do_test(test):
    global DATA_SERVICE_TEST_URL
    result = requests.post(
        DATA_SERVICE_TEST_URL,
        json={"question": test},
        headers={"Content-Type": "application/json"},
    )
    print(f'Performed test: "{test}"\n\tResult {result.json()}')
    return result.json()


def test_lore():
    global LORE_TESTS
    with concurrent.futures.ThreadPoolExecutor() as executor:
        all_results = list(executor.map(do_test, LORE_TESTS))

    print("Done")


if __name__ == "__main__":
    test_lore()
