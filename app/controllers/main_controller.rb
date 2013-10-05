class MainController < ApplicationController

	def index
	end

	def upload
		ip_address = request.remote_ip


		dir_string = "public/uploads/"+ip_address.to_s+"/"
		puts dir_string
		dir = File.dirname(dir_string)

		puts dir

		unless File.directory?(dir)
			puts 'Making directory!'
			FileUtils.mkdir_p(dir)
		end

		syllabi = ["1", "2", "3", "4", "5"]
		syllabi.each do |s|
			uploaded_io = params[s]
			if uploaded_io == nil
				next
			end
			File.open(Rails.root.join('public/uploads', ip_address, uploaded_io.original_filename), 'wb') do |file|
				unless File.directory?(file)
					puts 'Making directory!'
					FileUtils.mkdir_p(dir)
				end
				file.write(uploaded_io.read)
			end
		end

		value = %x(cat 'public/upload/18510.pdf' 2>&1)
		puts "BRYAN ESSS EL CABALLO!! ", value

		redirect_to dashboard_url
	end

	def dashboard
		@classes = ["18.404 Theory of Computation",
			"6.046 Design and Analysis of Algorithms",
			"21M.645 Motion Theater"]
	end

end
