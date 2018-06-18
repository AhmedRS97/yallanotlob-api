app = angular.module 'yallanotlob.app.home', ['yallanotlob.api']

app.controller 'AppHomeController', ['$scope', 'Meal', 'Order', ($scope, Meal, Order) ->
    $scope.meals = Meal.query()
    $scope.newOrder = new Order()
    $scope.save = ->
        angular.forEach $scope.newOrder, (obj, i) ->
            new Order({notes: obj.notes, meals: obj.meals[i]}).$save().then (result) ->
                $scope.orders.push result
        .then ->
            # Reset to a new blank Order.
            $scope.newOrder = new Order()
        .then ->
            # Clear any errors.
            $scope.errors = null
        , (rejection) ->
            $scope.errors = rejection.data
]
