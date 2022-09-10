from selene.support.shared import browser

def test_web_tables():
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Elena')
    browser.element('#lastName').type('Romanova')
    browser.element('#userEmail').type('elena@mail.ru')
    browser.element('#age').type('25')
    browser.element('#salary').type('250000')
    browser.element('#department').type('Insurance')
    browser.element('#submit').click()
    browser.element('#edit-record-2').click()
    browser.element('#firstName').clear().type('Oksana')
    browser.element('#lastName').clear().type('Volkova')
    browser.element('#userEmail').clear().type('oksana@mail.ru')
    browser.element('#age').clear().type('30')
    browser.element('#salary').clear().type('300000')
    browser.element('#department').clear().type('Insurance')
    browser.element('#submit').click()
    browser.element('#delete-record-3').click()




