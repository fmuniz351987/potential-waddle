#! /usr/bin/python3

'''
Simple script to run a CLI-based riffle program that reads through a CSV-like 
file that parses commends and tags from instagram and selects one person
as the winner.
'''

import re
from time import sleep
from random import choice
from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class Comment:
	author: str
	text: str
	tag: str

	def __hash__(self):
		return hash(self.author + self.tag)

	def __str__(self):
		return self.text


def roulette(iterable, n, interval):
	for i in range(n):
		sleep(interval)
		item = choice(iterable)
		print(item)
	return item

def winning_chance(iterable, author):
	total = len(iterable)
	by_author = len([c for c in iterable if c.author == author])
	return by_author, by_author / total

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('file', type=str)
	args = parser.parse_args()

	USERNAME = r'"?@[\w\d._]{1,30}'
	comments = set()
	pattern = re.compile(rf'^({USERNAME}):.*({USERNAME})')

	with open(args.file) as f:
		for line in f:
			result = pattern.match(line)
			if not result: continue		# comentário inválido sem nenhuma tag
			author = result.group(1)
			tagged = result.group(2)
			c = Comment(author=author, tag=tagged, text=line.strip())
			comments.add(c)
	
	comments = list(comments)
	roulette(comments, 50, 0.02)
	roulette(comments, 25, 0.04)
	roulette(comments, 10, 0.1)
	roulette(comments, 5, 0.2)
	roulette(comments, 4, 0.5)
	winner = roulette(comments, 1, 1)

	valid_comments, chance = winning_chance(comments, winner.author)
	chance *= 100
	print(f'Parabéns, {winner.author}! Você foi sorteado.')
	print(f'Você fez {valid_comments} comentários válidos e sua chance de ganhar era de {chance:.2f}%.')
