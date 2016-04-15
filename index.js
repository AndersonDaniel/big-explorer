angular.module('explorer', []).
	controller('mainController', ['$scope', '$http', '$interval', function($scope, $http, $interval) {
		var self = this;
		self.creating = false;
		
		self.newFileTypes = [
			{
				name: 'מסמך טקסט',
				type: 'txt'
			},
			{
				name: 'מסמך WORD',
				type: 'docx'
			},
			{
				name: 'תמונה',
				type: 'jpg'
			}
		];
		
		self.newFile = {};
		
		self.open = function(file) {
			$http.post('/open/' + file['name'] + '.' + file['type']);
			console.log('Opened ', file);
		};
		
		self.newfile = function() {
			self.creating = true;
		};
		
		self.cancelNewFile = function() {
			self.creating = false;
			self.newFile = {};
		};
		
		self.createNewFile = function() {
			$http.post('/create/' + self.newFile.name + '.' + self.newFile.type);
			self.load();
			self.cancelNewFile();
		};
		
		self.select = function(type) {
			self.newFile.type = type;
		};
		
		self.load = function() {
				$http.get('/files').then(function(data) {
				self.data = data.data;
			});
		};
		
		self.load();
		
		$interval(function () {
			$http.post('/alive');
		}, 10000);
	}]);