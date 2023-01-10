import React from 'react'
import Select from 'react-select'
import { useController, useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { string, number, z } from 'zod' // validation library
import "./inputForm.css"

const options = [
    { value: "1", label: "Yes"},
    { value: "0", label: "No"},
];

const schema = z.object({
    satisfaction_level: number().gte(0).lte(100).int(),
    last_evaluation: number().gte(0).lte(100).int(),
    number_project: number().int(),
    average_monthly_hours: number().int(),
    time_spend_company: number().int(),
    work_accident: string(),
    promotion_last_5year: string(),
    left: string(),
    salary_low: string(),
    salary_medium: string(),
});

const InputForm = ({onSave, user={}}) => {
  
  const {register, control, handleSubmit, formState} = useForm({defaultValues: user, resolver: zodResolver(schema)});

  const { field: work_accident_field } = useController({name: 'work_accident', control })
  const { field: promotion_last_5year_field } = useController({name: 'promotion_last_5year', control })
  const { field: left_field } = useController({name: 'left', control })
  const { field: salary_low_field } = useController({name: 'salary_low', control })
  const { field: salary_medium_field } = useController({name: 'salary_medium', control })
  
  const {errors} = formState

  const handleSelectChangeWorkAccident = (option) => {
    work_accident_field.onChange(option.value)
  };

  const handleSelectChangePromotion = (option) => {
    promotion_last_5year_field.onChange(option.value)
  };

  const handleSelectChangeLeft = (option) => {
    left_field.onChange(option.value)
  };

  const handleSelectChangeSalaryLow = (option) => {
    salary_low_field.onChange(option.value)
  };

  const handleSelectChangeSalaryMedium = (option) => {
    salary_medium_field.onChange(option.value)
  };

  const handleSave = (formValues) => {
    onSave(formValues)
  };

  return (
    <form className='Form' onSubmit={handleSubmit(handleSave)}>
        
            <p>What was the employee's satisfaction level from 0 to 100 ?</p>
            <input {...register('satisfaction_level', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.satisfaction_level?.message}</div>
            <p>What was the last evalutioan by the model ?</p>
            <input {...register('last_evaluation', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.last_evaluation?.message}</div>
            <p>How many projects has the employee worked on ?</p>
            <input {...register('number_project', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.number_project?.message}</div>
            <p>How many monthly work hours did the emloyee have ?</p>
            <input {...register('average_monthly_hours', { valueAsNumber: true } )} />
            <div style={{color: "red"}}>{errors.average_monthly_hours?.message}</div>
            <p>How much time did the employee spend in the company in years ?</p>
            <input {...register('time_spend_company', { valueAsNumber: true })} />
            <div style={{color: "red"}}>{errors.time_spend_company?.message}</div>
            <p>Has there ever been a work accident ?</p>
            <div>
                <Select
                value={options.find(({ value }) => value === work_accident_field.label)}
                onChange={handleSelectChangeWorkAccident}
                options={options}
                />
            </div>
            <p>Has the employee gotten a promotion in the last 5 years ?</p>
            <div>
                <Select
                value={options.find(({ value }) => value === promotion_last_5year_field.label)}
                onChange={ handleSelectChangePromotion}
                options={options}
                />
            </div>
            <p>Has the employee left the company on his own ?</p>
            <div>
                <Select
                value={options.find(({ value }) => value === left_field.label)}
                onChange={ handleSelectChangeLeft}
                options={options}
                />
            </div>
            <p>Was the salary low ?</p>
            <div>
                <Select
                value={options.find(({ value }) => value === salary_low_field.label)}
                onChange={ handleSelectChangeSalaryLow}
                options={options}
                />
            </div>
            <p>Was the salary medium ?</p>
            <div>
                <Select
                value={options.find(({ value }) => value === salary_medium_field.label)}
                onChange={ handleSelectChangeSalaryMedium}
                options={options}
                />
            </div>
            
            <button type="submit">Submit</button>
    </form>
  )
}

export default InputForm

