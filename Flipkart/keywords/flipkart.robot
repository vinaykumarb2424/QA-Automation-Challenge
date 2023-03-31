*** Settings ***

Documentation     Keywords supported for flipart Application to test testcases

*** Keywords ***
I do search product and verify
    [Arguments]  ${Client}      ${product_name}
    Call Method    ${Client}    search_product      ${product_name}
    Call Method    ${Client}    verify_product_search    ${product_name}

I do filter the price
    [Arguments]  ${Client}      ${price}
    Call Method    ${Client}    filter_products    ${price}

I do View the product from the list
    [Arguments]     ${Client}      ${price}
    Call Method     ${Client}    click_3rd_product    #${price}

I do add product to the cart and verify
    [Arguments]     ${Client}
    Call Method     ${Client}    add_cart
    ${result}=      Call Method     ${Client}    verify_cart
    [RETURN]      ${result}

