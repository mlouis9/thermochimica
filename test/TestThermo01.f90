

    !-------------------------------------------------------------------------------------------------------------
    !
    ! DISCLAIMER
    ! ==========
    ! 
    ! All of the programming herein is original unless otherwise specified.  Details of contributions to the 
    ! programming are given below.
    !
    !
    ! Revisions:
    ! ==========
    ! 
    !    Date          Programmer          Description of change
    !    ----          ----------          ---------------------
    !    02/07/2012    M.H.A. Piro         Original code
    !    11/07/2018    B.W.N. Fitzpatrick  Changed to a C-O database 
    !
    ! Purpose:
    ! ========
    !
    ! The purpose of this unit test is to ensure that Thermochimica does not proceed when the data file isn't
    ! specified
    !
    !-------------------------------------------------------------------------------------------------------------

program TestThermo01

    USE ModuleThermoIO

    implicit none
        
    ! Initialize variables:
    dTemperature            = 300D0
    dPressure               = 1D0    
    dElementMass            = 1D0
    cInputUnitTemperature   = 'K'
    cInputUnitPressure      = 'atm'
    CInputUnitMass          = 'moles'
    ! cThermoFileName       = '../data/C-O.dat'
    
    
    ! Parse the ChemSage data-file:
    call ParseCSDataFile(cThermoFileName)
        
    ! Call Thermochimica:
    call Thermochimica
    
    if (INFOThermo == 6) then
        ! The unit test passed: the correct error code was reported and exited gracefully.
        print *, 'TestThermo01: PASS'
    else
        ! The unit test failed.
        print *, 'TestThermo01: FAIL <---'
    end if
    
    ! Reset Thermochimica:
    call ResetThermo
    
end program TestThermo01