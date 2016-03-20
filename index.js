angular.module('explorer', []).
	controller('mainController', ['$scope', '$http', function($scope, $http) {
		var self = this;
		self.bla = 'shtut';
		
		self.open = function(file) {
			$http.post('/open/' + file['name'] + '.' + file['type']);
			console.log('Opened ', file);
		};
		
		self.newfile = function() {
			alert('creating new file');
		};
		
		$http.get('/files').then(function(data) {
			self.data = data.data;
		});
	}]);