# -- coding: UTF-8 --

import pandas as pd
import csv
from os import system, name 
from subprocess import call 
	
def clear(): 
	_ = call('clear' if name =='posix' else 'cls') 

def save_file(df_criteria):
	print('\n\nO arquivo esta sendo salvo...\n')
	df_criteria.to_csv('criterios_inclusao_exclusao.csv', index=False)

def separate_files(df_criteria):

	incluir = df_criteria[~df_criteria['Exclusion'].notna()]
	incluir.to_csv('artigos_incluidos.csv')
	
	excluir = df_criteria[df_criteria['Exclusion'].notna()]
	excluir.to_csv('artigos_excluidos.csv')

def main():
	df = pd.read_csv('My Library.csv')
	df = df[[ 'DOI', 'Url','Title', 'Abstract Note', 'Author', 'Publication Year']]

	# verify if you have already started doing the RSL
	try:
		print('Verificando se voce ja comecou o trabalho..')
		df_done = pd.read_csv('criterios_inclusao_exclusao.csv')
		print(f'Voce ja tem {len(df_done)} artigos concluidos. Parabens!')
		done_ids = df_done['ID'].to_list()
		df_criteria = df_done
	except:
		print('Voce ainda nao tem nenhum artigo avaliado. Bom trabalho!')
		done_ids = []
		df_criteria = pd.DataFrame()

	input('\nClique para continuar..')

	try:
		for ix, row in df.iterrows():

			if ix+1 not in done_ids:
				clear()
				print(f'Artigo {ix+1} de {len(df)}')
				print('\n--- Title ---')
				print(row['Title'])
				print('\n--- Abstract ---')
				print(row['Abstract Note'])
				print('\n-------------')
				inclusion = input('--> Inclusao: ')
				exclusion = input('--> Exclusao: ')

				data = {
					'ID': ix+1,
					'Author': row['Author'],
					'Title': row['Title'],
					'DOI': row['DOI'],
					'URL': row['Url'],
					'Publication Year': row['Publication Year'],
					'Inclusion': [inclusion],
					'Exclusion': [exclusion]
				}
				
				if df_criteria.empty:
					print('Salvando primeiro artigo..')
					df_criteria = pd.DataFrame.from_dict(data=data)
				else:
					df_criteria = df_criteria.append(pd.DataFrame.from_dict(data=data), ignore_index=True)

				input('\nClique para continuar.. (CTRL+C para finalizar)')

		else:
			save_criteria(df_criteria)
				
	except:
		save_criteria(df_criteria)

if __name__ == '__main__':
	main()