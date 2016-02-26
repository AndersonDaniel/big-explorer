angular.module('explorer', []).
	controller('mainController', ['$scope', '$http', function($scope, $http) {
		var self = this;
		self.bla = 'shtut';
		
		$http.get('/files').then(function(data) {
			self.data = data.data;
		});
	}]);