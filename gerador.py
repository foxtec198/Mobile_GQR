from flet import *

def GeradorQR(page: Page):
    def login(e):
        print('Login Realizado')
        
    page.title = 'Gerador QR'
    page.padding = 70
    
    icon = Icon(name=icons.QR_CODE_SCANNER,size=100)
    inServer = TextField(label="Servidor")
    inUser = TextField(label="Usuário")
    inPwd = TextField(label="Senha", password=True, can_reveal_password=True)
    salvarUser = Checkbox(label='Salvar Usuário')
    btnLogin = FilledButton('Login', icon='login', on_click = login)
    
    cardLogin = Container(
        content=Column([icon, inServer, inUser, inPwd, salvarUser, btnLogin]),
        bgcolor = 'Black',
        width = 300,
        height= 450,
        border_radius=20,
        padding = 20
    )
    page.add(Column([cardLogin]))

if __name__ == '__main__':
    app(GeradorQR)