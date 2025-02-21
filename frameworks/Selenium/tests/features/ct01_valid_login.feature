@valid_login
Feature: Login no sistema Orange HRM

  Scenario: Usuário realiza login com credenciais válidas
    Given que o usuário está na página de login do Orange HRM
    When ele insere um usuário válido "admin" e uma senha válida "admin123"
    And clica no botão "Login"
    Then ele deve ser redirecionado para o dashboard do sistema
