import click, requests, sys
from bs4 import BeautifulSoup

def get(url, phase, session, follow=False):
    try :
        r = session.get(url, verify=False, allow_redirects=follow)
        r.raise_for_status()
        return r
    except requests.exceptions.HTTPError as e:
        print('Error in phase {}'.format(phase))
        print(" ERROR ".center(80, "-"))
        print(e, file=sys.stderr)
        raise e
    except requests.exceptions.RequestException as e:
        print('Error in phase {}'.format(phase))
        print(e, file=sys.stderr)
        raise e

def post(url, headers, payload, phase, session):
    try :
        r = session.post(url, headers=headers, data=payload, verify=False, allow_redirects=False)
        r.raise_for_status()
        return r
    except requests.exceptions.HTTPError as e:
        print('Error in phase {}'.format(phase))
        print(" ERROR ".center(80, "-"))
        print(e, file=sys.stderr)
        raise e
    except requests.exceptions.RequestException as e:
        print('Error in phase {}'.format(phase))
        print(e, file=sys.stderr)
        raise e

def run(username, password, env, target):

    print('starting...')
    with requests.Session() as s:

        base_url = 'https://login.internal.{}.k8s.cedacrigroup.it'.format(env)
        internal_url = 'https://dex.internal.{}.k8s.cedacrigroup.it'.format(env)

        #GET LOGIN
        r_login = get(base_url + '/login', 'get login page', s, True)
        soup = BeautifulSoup(r_login.text, 'html.parser')
        login_form_action = soup.find('form').get('action')

        #DO LOGIN
        r_dologin = post(internal_url + login_form_action, {}, {'login': username, 'password': password}, 'submitting form', s)
        soup = BeautifulSoup(r_dologin.text, 'html.parser')
        print(soup)
        if soup.find(id='login-error'):
            raise Exception(soup.find(id='login-error').text.strip())

        #FWD 1
        r_fwd1 = get(internal_url + r_dologin.headers.get('Location'), 'forward 1', s)
        #FWD 2
        r_fwd2 = get(r_fwd1.headers.get('Location'), 'forward 2', s)
        #FWD 3
        r_fwd3 = get(base_url + r_fwd2.headers.get('Location'), 'forward 3', s)
        #DOWNLOAD KUBECONF
        r_download = get(base_url + '/kubeconf', 'download kubeconf', s)

        with open(target, "w") as text_file:
            text_file.write(r_download.text)

    print("done!")

@click.command()
@click.option("--username", prompt=True)
@click.option("--password", prompt=True, hide_input=True)
@click.option("--env", type=click.Choice(['svl', 'col', 'ads', 'prd']), required=True)
@click.option('--target', help="The target file", default='kubeconf', show_default=True)
def main(username, password, env, target):
    run(username, password, env, target)

if __name__ == "__main__":
    main()
