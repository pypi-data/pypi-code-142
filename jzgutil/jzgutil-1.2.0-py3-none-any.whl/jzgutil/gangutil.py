import click, requests, sys
from bs4 import BeautifulSoup

def run(username, password, env, target):
    print("starting...")

    def get(url, phase):
        try :
            r = s.get(url, verify=False, allow_redirects=False)
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

    with requests.Session() as s:

        hs = {
            'Content-type': 'application/x-www-form-urlencoded', 
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

        pl = {'login': username, 'password': password}

        base_url = 'https://login.internal.{}.k8s.cedacrigroup.it'.format(env)
        internal_url = 'https://dex.internal.{}.k8s.cedacrigroup.it'.format(env)

        #GET LOGIN
        r_login = s.get(base_url + '/login', verify=False, allow_redirects=True)
        r_login.raise_for_status()
        soup = BeautifulSoup(r_login.text, 'html.parser')
        login_form_action = soup.find('form').get('action')

        #DO LOGIN
        r_dologin = s.post(internal_url + login_form_action, headers=hs, data=pl, verify=False, allow_redirects=False)
        r_dologin.raise_for_status()

        #FWD 1
        r_fwd1 = get(internal_url + r_dologin.headers.get('Location'), 'forward 1')

        #FWD 2
        r_fwd2 = get(r_fwd1.headers.get('Location'), 'forward 2')

        #FWD 3
        r_fwd3 = get(base_url + r_fwd2.headers.get('Location'), 'forward 3')

        #DOWNLOAD KUBECONF
        r_download = s.get(base_url + '/kubeconf', verify=False, allow_redirects=False)
        r_download.raise_for_status()

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
