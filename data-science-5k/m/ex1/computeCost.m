
% /Users/davebabbitt/Notebooks/data-science-5k/m/ex1/computeCost.m
function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

% J(θ)= 1   hθ(x(i))−y(i) 2
%       2m i=1
for i=1:m,

% The hypothesis (also called the prediction) is simply the product of X and theta
prediction = theta' * X(i,:)';

% Compute the difference between the hypothesis and y
% (that's the error for each training example)
error = prediction - y(i);

% Compute the square of each of those error terms (using element-wise exponentiation)
J = J + error^2;

end;
J = J/(2*m);

% Above works; trying to grok vectorization

% The hypothesis (also called the prediction) is simply the product of X and theta
H = (X*theta);

% Compute the square of each of those error terms (using element-wise exponentiation)
S = sum((H-y).^2);

J = S / (2*m);

% =========================================================================

end
