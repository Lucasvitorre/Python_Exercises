from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Se modificar esses escopos, exclua o arquivo token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    """Obtém as credenciais do usuário ou solicita autorização."""
    creds = None
    # O arquivo token.json armazena as credenciais do usuário.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Se não houver credenciais válidas, o usuário deverá fazer login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva as credenciais para a próxima execução
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_event(service):
    #Cria um evento no Google Calendar.#
    event = {
      'summary': 'Reunião com o cliente',
      'location': '800 Howard St., San Francisco, CA 94103',
      'description': 'Discussão sobre o novo projeto.',
      'start': {
        'dateTime': '2024-07-02T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2024-07-02T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
      ],
      'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Evento criado: %s' % (event.get('htmlLink')))

def main():
    """Autentica e cria um evento no Google Calendar."""
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    create_event(service)

if __name__ == '__main__':
    main()
