export default function Input({
  id,
  name,
  label,
  type = 'text',
  value,
  onChange,
  placeholder = '',
  error = '',
  hint = '',
  required = false,
  autoComplete,
  className = '',
  ...props
}) {
  return (
    <div className={`form-group ${className}`.trim()}>
      {label && (
        <label htmlFor={id}>
          {label} {required && <span style={{ color: 'var(--status-danger)' }}>*</span>}
        </label>
      )}
      <input
        id={id}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        autoComplete={autoComplete}
        required={required}
        className={`form-input ${error ? 'error' : ''}`}
        {...props}
      />
      {error && <span className="form-error">{error}</span>}
      {hint && !error && <span className="form-hint">{hint}</span>}
    </div>
  );
}
