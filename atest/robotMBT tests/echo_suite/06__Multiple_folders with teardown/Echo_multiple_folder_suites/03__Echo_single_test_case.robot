*** Settings ***
Suite Teardown       Set Global Variable    ${teardown_count}    ${teardown_count+1}

*** Test Cases ***
first test case
    Set Global Variable    ${test_count}    ${test_count+1}
