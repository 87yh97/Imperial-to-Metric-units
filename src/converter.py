import click



@click.command()
@click.option(  '--from',
                'source_unit_arg', 
#                default='ft', 
                help='What imperial unit to convert from', 
                required=True
)
@click.option(  '--to', 
                'target_unit_arg', 
#                default='m', 
                help='What metric unit to convert to', 
                required=True
)
def converter(source_unit_arg, target_unit_arg):
#    if source_unit_arg == 'ft':
    source_unit_val = click.prompt('Source unit', type=float)
    print("Target unit value: {:f}".format(source_unit_val / 3.281))





if __name__ == '__main__':
    converter()

