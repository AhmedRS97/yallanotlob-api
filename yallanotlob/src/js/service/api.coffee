app = angular.module 'yallanotlob.api', ['ngResource']

app.factory 'Meal', ['$resource', ($resource) ->
    $resource '/api/meals/:id', id: '@id'
]

app.factory 'Order', ['$resource', ($resource) ->
    $resource '/api/orders/:id', id: '@id'
]

# And the nested resources
app.factory 'OrderMeal', ['$resource', ($resource) ->
    $resource '/api/orders/:id/meals/'
]
