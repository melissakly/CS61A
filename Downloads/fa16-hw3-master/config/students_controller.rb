class StudentsController < ApplicationController
	def home
	end
	
  def new
    @placeholder_full_name = "Melissa Ly"
    @placeholder_course = "rails"
    @placeholder_grade_level = "soph"
  end

  def create
    @full_name = params[:full_name]
    @course = params[:course]
    @grade_level = param[:grade_level]
    render 'show'
  end
end
