class MainController < ApplicationController

	def index
	end

	def upload
		syllabi = ["1", "2", "3", "4", "5"]
		syllabi.each do |s|
			puts s
			uploaded_io = params[s]
			if uploaded_io == nil
				next
			end
			File.open(Rails.root.join('public', 'uploads', uploaded_io.original_filename), 'wb') do |file|
			file.write(uploaded_io.read)
			end
		end

		value = %x(pwd 2>&1)
		puts "BRYAN ESSS EL CABALLO!! ", value

		redirect_to dashboard_url
	end

	def dashboard
		@classes = ["18.404 Theory of Computation",
			"6.046 Design and Analysis of Algorithms",
			"21M.645 Motion Theater"]
	end

end
