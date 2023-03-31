*** Settings ***
Library         ../../Flipkart/library/Flipkart.py      WITH NAME       client1
Resource        ../../Flipkart/keywords/flipkart.robot

*** Variables ***
${product}      samsung mobiles
*** Keywords ***
Create Instance
    $Client     = Get Library Instance      client1
    Set Suite Variable    $Client
*** Test Cases ***
TC-1: Search Product and Verify
    ${Client}=      Get Library Instance    client1
    Set Suite Variable    ${Client}
    I do search product and verify  ${Client}   ${product}
TC-2: Filter price and Verify
    I do filter the price       ${Client}        ₹20000

TC-3: View the product from the list
    I do View the product from the list     ${Client}    1

TC-4: Add product to the cart and verify
    ${result}=    I do add product to the cart and verify     ${Client}
    Log To Console    ${result}

