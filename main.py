from itertools import combinations

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


pot_d = {
    'SEA',
    'LV',
    'CIN',
    'HOU',
    'LAR',
    'LAC',
    'ARI',
    'MIN',
    'CHI',
    'PHI',
    'WSH',
    'NYG',
    'CAR',
    'DEN',
    'BAL',
    'NE',
    'IND',
    'GB',
    'DET',
    'NYJ',
    'TEN',
}

target_opp = {
    'LV',
    'CAR',
    'NYJ',
    'PIT',
    'CHI',
    'NYG',
    'HOU',
}

weekly_games = [
    { # week 3
        'LV': 'PIT',
        'CAR': 'SEA',
        'NYJ': 'NE',
        'CHI': 'KC',
        'NYG': 'SF',
        'TEN': 'CLE',
    },
    { # week 4
        'LV': 'LAC',
        'CAR': 'MIN',
        'NYJ': 'KC',
        'PIT': 'HOU',
        'CHI': 'DEN',
        'NYG': 'SEA',
        'TEN': 'CIN',
    },
    { # week 5
        'LV': 'GB',
        'CAR': 'DET',
        'NYJ': 'DEN',
        'PIT': 'BAL',
        'CHI': 'WAS',
        'NYG': 'MIA',
        'TEN': 'IND',
    },
    { # week 6
        'LV': 'NE',
        'CAR': 'MIA',
        'NYJ': 'PHI',
        'CHI': 'MIN',
        'NYG': 'BUF',
        'TEN': 'BAL',
    },
    { # week 7
        'LV': 'CHI',
        'PIT': 'LAR',
        'CHI': 'LV',
        'NYG': 'WAS',
    },
    { # week 8
        'LV': 'DET',
        'CAR': 'HOU',
        'NYJ': 'NYG',
        'PIT': 'JAX',
        'CHI': 'LAC',
        'TEN': 'ATL',
    },
    { # week 9
        'LV': 'NYG',
        'CAR': 'IND',
        'NYJ': 'LAC',
        'PIT': 'TEN',
        'CHI': 'NO',
    },
    { # week 10
        'LV': 'NYJ',
        'CAR': 'CHI',
        'PIT': 'GB',
        'NYG': 'DAL',
        'TEN': 'TB',
    },
]

def opp(team, week):
    for team1, team2 in week.items():
        if team == team1:
            return team2
        elif team == team2:
            return team1
    return None


def weeks_covered(defenses):
    weeks_covered = 0
    for week in weekly_games:
        for defense in defenses:
            if opp(defense, week) in target_opp:
                weeks_covered += 1
                break
    return weeks_covered


def main():
    results = {}
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    for combo in combinations(pot_d, 3):
        results[combo] = weeks_covered(combo)

    print(len(results))
    d_view = [(v, k) for k, v in results.items()]
    d_view.sort(reverse=True)  # natively sort tuples by first element
    for v, k in d_view:
        print(f'{v}: {k}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
