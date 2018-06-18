app = angular.module 'yallanotlob.app.home', ['yallanotlob.api']

app.controller 'AppOrderController', ['$scope', 'Order', ($scope, Order) ->
    $scope.orders = Order.query()
]
