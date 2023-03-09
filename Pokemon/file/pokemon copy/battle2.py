import pokemon
import pokemon.battle

if __name__ == '__main__':
    red_team = pokemon.battle.Team([
        pokemon.Pokemon(pokemon.find_species('charizard'), level=90, moves=[
            pokemon.find_move(move) for move in (
                'bubble beam', 'hydro pump', 'water gun', 'waterfall')])])
    blue_team = pokemon.battle.Team([
        pokemon.Pokemon(pokemon.find_species('squirtle'), level=10, moves=[
            pokemon.find_move(move) for move in (
                'tackle', 'tail whip', 'bubble', 'water gun')]), pokemon.Pokemon(pokemon.find_species('squirtle'), level=10, moves=[
            pokemon.find_move(move) for move in (
                'tackle', 'tail whip', 'bubble', 'water gun')]) ])
    teams = (red_team, blue_team)

    while not any(team.blacked_out() for team in teams):
        for team in teams:
            print(f'{team.fighter.name} has {team.fighter.hp} hp')
        move_choices = []
        for i, team in enumerate(teams):
            other_team = teams[(i + 1) % 2]
            print(f'What will {team.fighter.name} do?')
            print(*list(team.fighter.moves.keys()), sep='\n')
            move_name = input('>> ')
            move_choices.append(pokemon.battle.MoveChoice(
                fighter=team.fighter, move=move_name, target=other_team.fighter))
        for result in pokemon.battle.fight(move_choices):
            print(f'{result.move_choice.fighter.name} used {result.move_choice.move}!')
            if result.miss:
                print(f'{result.move_choice.move} missed!')
                continue
            if result.damage.critical_hit:
                print('Critical hit!')
            print(f'{result.damage.effectiveness}x effective')
            if result.ko:
                print(f'{result.move_choice.target.name} died!')
            else:
                print(f'{result.move_choice.target.name} now has {result.move_choice.target.hp} hp')
        print('\n==================\n')

    if red_team.blacked_out():
        print(f'Red blacked out!')
    elif blue_team.blacked_out():
        print(f'Blue blacked out!')
