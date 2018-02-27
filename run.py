from hashcode import parser


test = parser.Parser('Resources/small.in')
pizza = test.make_pizza()
print(pizza.get_grid())
pizza.print_config()

