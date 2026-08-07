# api_test.ps1

$ErrorActionPreference = "Stop"

$ApiBase = "http://localhost:5000"

Write-Host ""
Write-Host "========================================="
Write-Host "PROPERTY MANAGER API TEST SUITE"
Write-Host "========================================="
Write-Host ""

function Print-Json {
    param($Object)

    $Object | ConvertTo-Json -Depth 10
}

try {

    # -------------------------------------------------
    # TENANTS
    # -------------------------------------------------

    Write-Host "[TENANTS] CREATE"

    $tenantBody = @{
        first_name   = "Kwanele"
        last_name    = "Zikhali"
        phone_number = "0823333333"
        email        = "kwanele@example.com"
    } | ConvertTo-Json

    $tenant = Invoke-RestMethod `
        -Method POST `
        -Uri "$ApiBase/api/tenants/" `
        -ContentType "application/json" `
        -Body $tenantBody

    $tenantId = $tenant.id

    Print-Json $tenant

    Write-Host ""
    Write-Host "[TENANTS] GET ALL"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/tenants/"
    )

    Write-Host ""
    Write-Host "[TENANTS] GET BY ID"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/tenants/$tenantId"
    )

    Write-Host ""
    Write-Host "[TENANTS] PATCH"

    $tenantPatch = @{
        phone_number = "0834444444"
    } | ConvertTo-Json

    Print-Json (
        Invoke-RestMethod `
            -Method PATCH `
            -Uri "$ApiBase/api/tenants/$tenantId" `
            -ContentType "application/json" `
            -Body $tenantPatch
    )

    # -------------------------------------------------
    # PROPERTIES
    # -------------------------------------------------

    Write-Host ""
    Write-Host "[PROPERTIES] CREATE"

    $propertyBody = @{
        name        = "Benjamin Court"
        address     = "123 Main Road"
        city        = "Durban"
        province    = "KwaZulu-Natal"
        postal_code = "4001"
    } | ConvertTo-Json

    $property = Invoke-RestMethod `
        -Method POST `
        -Uri "$ApiBase/api/properties/" `
        -ContentType "application/json" `
        -Body $propertyBody

    $propertyId = $property.id

    Print-Json $property

    Write-Host ""
    Write-Host "[PROPERTIES] GET ALL"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/properties/"
    )

    Write-Host ""
    Write-Host "[PROPERTIES] GET BY ID"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/properties/$propertyId"
    )

    Write-Host ""
    Write-Host "[PROPERTIES] PATCH"

    $propertyPatch = @{
        address = "456 Smith Street"
    } | ConvertTo-Json

    Print-Json (
        Invoke-RestMethod `
            -Method PATCH `
            -Uri "$ApiBase/api/properties/$propertyId" `
            -ContentType "application/json" `
            -Body $propertyPatch
    )

    # -------------------------------------------------
    # LEASES
    # -------------------------------------------------

    Write-Host ""
    Write-Host "[LEASES] CREATE"

    $leaseBody = @{
        tenant_id    = $tenantId
        property_id  = $propertyId
        start_date   = "2026-01-01"
        end_date     = "2026-12-31"
        monthly_rent = 9000
    } | ConvertTo-Json

    $lease = Invoke-RestMethod `
        -Method POST `
        -Uri "$ApiBase/api/leases/" `
        -ContentType "application/json" `
        -Body $leaseBody

    $leaseId = $lease.id

    Print-Json $lease

    Write-Host ""
    Write-Host "[LEASES] GET ALL"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/leases/"
    )

    Write-Host ""
    Write-Host "[LEASES] GET BY ID"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/leases/$leaseId"
    )

    Write-Host ""
    Write-Host "[LEASES] PATCH"

    $leasePatch = @{
        monthly_rent = 9500
    } | ConvertTo-Json

    Print-Json (
        Invoke-RestMethod `
            -Method PATCH `
            -Uri "$ApiBase/api/leases/$leaseId" `
            -ContentType "application/json" `
            -Body $leasePatch
    )

    # -------------------------------------------------
    # PAYMENTS
    # -------------------------------------------------

    Write-Host ""
    Write-Host "[PAYMENTS] CREATE"

    $paymentBody = @{
        lease_id       = $leaseId
        amount         = 9500
        payment_date   = "2026-08-01"
        payment_method = "EFT"
        reference      = "AUG-2026"
    } | ConvertTo-Json

    $payment = Invoke-RestMethod `
        -Method POST `
        -Uri "$ApiBase/api/payments/" `
        -ContentType "application/json" `
        -Body $paymentBody

    $paymentId = $payment.id

    Print-Json $payment

    Write-Host ""
    Write-Host "[PAYMENTS] GET ALL"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/payments/"
    )

    Write-Host ""
    Write-Host "[PAYMENTS] GET BY ID"

    Print-Json (
        Invoke-RestMethod `
            -Method GET `
            -Uri "$ApiBase/api/payments/$paymentId"
    )

    Write-Host ""
    Write-Host "[PAYMENTS] PATCH"

    $paymentPatch = @{
        amount    = 10000
        reference = "UPDATED-AUG-2026"
    } | ConvertTo-Json

    Print-Json (
        Invoke-RestMethod `
            -Method PATCH `
            -Uri "$ApiBase/api/payments/$paymentId" `
            -ContentType "application/json" `
            -Body $paymentPatch
    )

    # -------------------------------------------------
    # DELETES
    # -------------------------------------------------

    Write-Host ""
    Write-Host "[PAYMENTS] DELETE"

    $response = Invoke-WebRequest `
        -Method DELETE `
        -Uri "$ApiBase/api/payments/$paymentId"

    $response.StatusCode

    Write-Host ""
    Write-Host "[LEASES] DELETE"

    $response = Invoke-WebRequest `
        -Method DELETE `
        -Uri "$ApiBase/api/leases/$leaseId"

    $response.StatusCode

    Write-Host ""
    Write-Host "[PROPERTIES] DELETE"

    $response = Invoke-WebRequest `
        -Method DELETE `
        -Uri "$ApiBase/api/properties/$propertyId"

    $response.StatusCode

    Write-Host ""
    Write-Host "[TENANTS] DELETE"

    $response = Invoke-WebRequest `
        -Method DELETE `
        -Uri "$ApiBase/api/tenants/$tenantId"

    if ($response.Content) {
        $response.Content
    }
    else {
        $response.StatusCode
    }

    Write-Host ""
    Write-Host "========================================="
    Write-Host "ALL TESTS COMPLETED"
    Write-Host "========================================="
}
catch {
    Write-Host ""
    Write-Host "========================================="
    Write-Host "TEST FAILED"
    Write-Host "========================================="
    Write-Host $_.Exception.Message

    if ($_.ErrorDetails.Message) {
        Write-Host $_.ErrorDetails.Message
    }

    throw
}
