*** Settings ***
Suite Setup       Treat this test suite Model-based
Library           robotmbt    processor=echo

*** Test Cases ***
first test case
    Set Global Variable    ${test_count}    ${test_count+1}

second test case
    Set Global Variable    ${test_count}    ${test_count+1}

third test case
    Set Global Variable    ${test_count}    ${test_count+1}
