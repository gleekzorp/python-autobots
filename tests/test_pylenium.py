

def test_fake_stuff(fake):
    first_name = fake.first_name()
    print(first_name)
    print(fake.address())
    print(fake.ssn())
    print(fake.name())
    print(fake.email())


def test_request_stuff(py, api):
    response = py.request.get('/cards')
    assert response.ok
